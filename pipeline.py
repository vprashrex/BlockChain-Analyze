import aiohttp
import asyncio
import pandas as pd
from openpyxl import Workbook


class FetchAnalyze:
    API_URL = "https://api.coingecko.com/api/v3/coins/markets"
    EXCEL_FILE = "crypto_live_data.xlsx"
    UPDATE_INTERVAL = 300  # 5 minutes in seconds

    async def _fetch_crypto_data(self):
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 50,
            'page': 1
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.API_URL, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    raise Exception(f"Failed to fetch data: {response.status}")

    def _analyze_data(self, data):
        df = pd.DataFrame(data)
        top_5 = df.nlargest(5, 'market_cap')
        avg_price = df['current_price'].mean()
        highest_change = df.nlargest(1, 'price_change_percentage_24h')
        lowest_change = df.nsmallest(1, 'price_change_percentage_24h')
        return top_5, avg_price, highest_change, lowest_change

    def _update_excel(self, data):
        df = pd.DataFrame(data)
        df.to_excel(self.EXCEL_FILE, index=False)
        print("Excel updated!")

    async def main(self):
        while True:
            try:
                crypto_data = await self._fetch_crypto_data()
                top_5, avg_price, high_change, low_change = self._analyze_data(crypto_data)

                print("Top 5 Cryptocurrencies:")
                print(top_5[['name', 'current_price', 'market_cap']])
                print(f"Average Price: ${avg_price:.2f}")
                print("Highest Change (24h):", high_change[['name', 'price_change_percentage_24h']])
                print("Lowest Change (24h):", low_change[['name', 'price_change_percentage_24h']])

                self._update_excel(crypto_data)

                await asyncio.sleep(self.UPDATE_INTERVAL)

            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    fetch_obj = FetchAnalyze()
    asyncio.run(fetch_obj.main())