import os

def base_directories():
    openadk_dir = os.path.join(
        os.path.dirname(__file__),
        "..", "modules", "openadk",
    )
    assert os.path.exists(openadk_dir), openadk_dir
    config_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..", "config",
        )
    )
    assert os.path.exists(config_dir), config_dir
    return config_dir, openadk_dir
