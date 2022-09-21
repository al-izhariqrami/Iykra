from google.cloud import storage
import urllib.request

project_id = 'applied-well362908'
bucket_name = 'fellowship_77'
destination_blob_name = 'Izhar.jpg'
storage_client = storage.Client.from_service_account_json('applied-well-362908-84bd1b318dff.json')

source_file_name = 'https://www.wallpapergeeks.com/wp-content/uploads/2014/03/Nature_107.jpg'

def upload_blob(bucket_name, source_file_name, destination_blob_name):   
    file = urllib.request.urlopen(source_file_name).read()

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(file, content_type='image/jpg')

upload_blob(bucket_name, source_file_name, destination_blob_name)
