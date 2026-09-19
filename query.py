#!/usr/bin/env python3
"""Search the published snapshot without inferring or updating policy facts."""
import argparse
import csv
from datetime import date
import io
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

FIELDS = ('brand', 'return_window', 'return_postage', 'free_shipping_threshold',
          'opened_products', 'official_sources', 'reviewed_on')
POLICIES = FIELDS[1:5]

def load_snapshot(root):
    rows = json.loads((root / 'policies.json').read_text(encoding='utf-8-sig'))
    if not isinstance(rows, list) or not rows:
        raise ValueError('policies.json must contain a nonempty array')
    seen = set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != set(FIELDS):
            raise ValueError('Unexpected fields in JSON record')
        if any(not isinstance(row[k], str) or not row[k] for k in FIELDS if k != 'official_sources'):
            raise ValueError('Policy text, brand and review date must be nonempty strings')
        key = row['brand'].casefold()
        if key in seen:
            raise ValueError('Duplicate brand: ' + row['brand'])
        seen.add(key)
        date.fromisoformat(row['reviewed_on'])
        sources = row['official_sources']
        if not isinstance(sources, dict) or set(sources) != set(POLICIES):
            raise ValueError('Unexpected official_sources fields')
        for links in sources.values():
            if not isinstance(links, list) or any(not isinstance(u, str) or urlsplit(u).scheme not in ('http', 'https') or not urlsplit(u).netloc for u in links):
                raise ValueError('Invalid source URL list')
    with (root / 'policies.csv').open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if tuple(reader.fieldnames or []) != FIELDS:
            raise ValueError('Unexpected CSV fields')
        csv_rows = list(reader)
    for row in csv_rows:
        row['official_sources'] = json.loads(row['official_sources'])
    if csv_rows != rows:
        raise ValueError('CSV and JSON records differ')
    return rows

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--brand', default='', help='Case-insensitive brand substring')
    parser.add_argument('--format', choices=('json', 'csv'), default='json')
    parser.add_argument('--validate', action='store_true', help='Check schema and CSV/JSON equality only')
    args = parser.parse_args()
    try:
        rows = load_snapshot(args.data_dir)
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.exit(2, 'Validation failed: ' + str(error) + '\n')
    if args.validate:
        print(json.dumps({'valid': True, 'records': len(rows), 'fields': len(FIELDS)}))
        return 0
    selected = [row for row in rows if args.brand.casefold() in row['brand'].casefold()]
    if args.format == 'json':
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, lineterminator='\n')
        writer.writeheader()
        for row in selected:
            writer.writerow({**row, 'official_sources': json.dumps(row['official_sources'], ensure_ascii=False, separators=(',', ':'))})
    return 0 if selected else 1

if __name__ == '__main__':
    raise SystemExit(main())
