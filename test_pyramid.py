import boto3
from moto import mock_s3
import pytest
import os

from pyramid import Pyramid

PYRAMID_FULL_PATH = os.path.abspath('../pyramid')
DZI_PATH = os.path.abspath('../pyramid/pyramid.dzi')


@pytest.fixture(scope='function')
def s3_fixture():
    mocks3 = mock_s3()
    mocks3.start()

    client = boto3.client('s3')
    pyramid_bucket_name = 'pyramid'
    client.create_bucket(Bucket=pyramid_bucket_name)
    client.upload_file(DZI_PATH, pyramid_bucket_name, 'pyramid.dzi')

    def _upload_directory(path, bucket, s3_client):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                key = file_path.replace(PYRAMID_FULL_PATH+ '/', '')
                s3_client.upload_file(file_path, bucket, key)

    _upload_directory(os.path.abspath(f'{PYRAMID_FULL_PATH}/pyramid_files'), pyramid_bucket_name, client)

    yield client, pyramid_bucket_name

    mocks3.stop()


@pytest.fixture(scope='module')
def expected_read_result_shape_without_zoom():
    return 1800, 1400, 3
    #return 1400, 1400, 3 


@pytest.fixture(scope='module')
def expected_read_result_shape_with_zoom():
    return 920, 760, 3


def test_pyramid_read_without_zoom(expected_read_result_shape_without_zoom):
    # read from the pyramid the following rect: x_start=600 , y_start=600, x_end=2000, y_end=2400, zoom=1
    pyramid = Pyramid()
    region = [[600, 600], [2000,2400]]
    rect_data = pyramid.read(region)
    assert rect_data.shape == expected_read_result_shape_without_zoom


def test_pyramid_read_with_zoom(expected_read_result_shape_with_zoom):
    # read from the pyramid the following rect: x_start=100 , y_start=100, x_end=2000, y_end=2400, zoom=0.4
    # rect_data = pyramid.read(...)
    pyramid = Pyramid()
    region = [[100, 100], [2000,2400]]
    rect_data = pyramid.read(region, zoom=0.4)
    assert rect_data.shape == expected_read_result_shape_with_zoom


def test_pyramid_read_s3_without_zoom(s3_fixture, expected_read_result_shape_without_zoom):
#     # read from S3 pyramid the following rect: x_start=600 , y_start=600, x_end=2000, y_end=2400, zoom=1
        print(s3_fixture.list_objects(bucket_name = 'pyramid'))
        # assert rect_data.shape == expected_read_result_shape_without_zoom


# def test_pyramid_read_s3_with_zoom(s3_fixture, expected_read_result_shape_with_zoom):
#     # read from S3 pyramid the following rect: x_start=100 , y_start=100, x_end=2000, y_end=2400, zoom=0.4
#     assert rect_data.shape == expected_read_result_shape_with_zoom


# def test_1():
#     pyramid = Pyramid()
#     rect_data = pyramid.read([[600,600], [2000,2000]])
