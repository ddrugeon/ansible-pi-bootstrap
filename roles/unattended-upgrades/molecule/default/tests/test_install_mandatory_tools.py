import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize("name", [
    ("apt-transport-https"),
    ("software-properties-common"),
    ("unattended-upgrades"),
    ("mailutils"),
    ("bsd-mailx"),
])
def test_default_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_default_config_files_present(host):
    f = host.file("/etc/apt/apt.conf.d/50unattended-upgrades")
    assert f.exists
    assert f.is_file
