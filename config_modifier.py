from configparser import ConfigParser


def change_config(section_name, field_name, value):
    config = ConfigParser()
    config.read('config.ini')
    config.set(section_name, field_name, str(value))
    with open('./config.ini', 'w') as f:
        config.write(f)


def change_max_time(tm):
    change_config('run_settings', 'max_run_time', tm)


def change_max_asserts(num):
    change_config('run_settings', 'max_asserts', num)


def change_assert_warnings(num):
    change_config('run_settings', 'assert_warning', num)


def generate_default_config():
    config = ConfigParser()

    config['run_settings'] = {
        'max_run_time': '20000',  # in milliseconds
        'max_asserts': '10',
        'assert_warning': '5'
    }

    with open('./config.ini', 'w') as f:
        config.write(f)
