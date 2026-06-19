from datetime import datetime

def transform(raw_data:dict)->list:
    records=[]
    for key,value in raw_data.items():
        records.append({
            'coin': key,
            'price_usd': value['usd'],
            'usd_24h_change': round(value.get('usd_24h_change',0),3),
            'collected_at': datetime.utcnow()
        })
    return records

if __name__=='__main__':
    sample = {
        "bitcoin": {"usd": 65000, "usd_24h_change": 1.5},
        "ethereum": {"usd": 3500, "usd_24h_change": 0.8}
    }
    print(transform(sample))