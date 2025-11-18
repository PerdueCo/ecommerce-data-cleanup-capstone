import pandas as pd

def clean_sku(s):
    s = str(s).strip().upper().replace(' ', '').replace('-', '')
    return f"{s[:-3]}-{s[-3:]}" if len(s) > 3 else s

def clean_title(t):
    return ' '.join(str(t).title().split())

def clean_category(c):
    c = str(c).strip().title()
    mapping = {
        'Tires': 'Tires',
        'Pedal': 'Pedals',
        'Pedals': 'Pedals',
        'Accessories': 'Accessories',
        'Accessory': 'Accessories'
    }
    return mapping.get(c, c)

def main():
    df = pd.read_csv('data/raw_products.csv')

    df['sku'] = df['sku'].apply(clean_sku)
    df['title'] = df['title'].apply(clean_title)
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
    df['category'] = df['category'].apply(clean_category)
    df['inventory'] = pd.to_numeric(df['inventory'], errors='coerce').clip(lower=0).fillna(0)

    df['is_valid'] = df.apply(lambda r: 'YES' if r['price'] > 0 and r['sku'] != '' else 'NO', axis=1)

    df.to_csv('data/clean_products.csv', index=False)
    print('Cleanup complete.')

if __name__ == '__main__':
    main()
