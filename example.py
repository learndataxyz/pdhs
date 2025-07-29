from pdhs.datasets import GetDatasets 
from pdhs.download import DHSDownloader
import os
import asyncio

from dotenv import load_dotenv
load_dotenv()


dhs_password = os.getenv("DHS_PASSWORD")
# Main execution function
async def main():
    # Example usage
    indicators_data = GetDatasets(
        country_ids=["NG"],
        file_format="DT"
    )

    df = indicators_data.get_data()
    print(df)

    downloader = DHSDownloader(
        email="adejumo999@gmail.com",
        password=dhs_password,
        download_path="my_files",
        project_name="Rural and Urban",
        dataframe=df
    )

    dataset_ids = ['NGHW21DT.ZIP', 'NGBR21dt.zip', 'NGKR21DT.ZIP']
    await downloader.download_all_datasets(dataset_ids)

    # After downloading datasets
    dataset_id = 'NGHW21DT.ZIP'  # Example ZIP dataset
    df_loaded = downloader.load_dataset_as_dataframe(dataset_id)

    # Perform operations on the loaded DataFrame
    if df_loaded is not None:
        print(df_loaded.head())

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())