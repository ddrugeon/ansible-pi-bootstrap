import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_pi_password_enabled(host):
    f = host.file('/etc/sudoers.d/010_pi-passwd')
    assert f.is_file
    assert f.exists

    assert f.contains('pi ALL=(ALL) PASSWD: ALL')

def test_pi_no_password_disabled(host):
    f = host.file('/etc/sudoers.d/010_pi-nopasswd')
    assert f.contains('#pi ALL=(ALL) NOPASSWD: ALL')


def test_admin_users_no_password_disabled(host):
    f = host.file('/etc/sudoers.d/010_apple-nopasswd')
    assert f.is_file
    assert f.exists
    assert f.contains('apple ALL=(ALL) NOPASSWD: ALL')

    f = host.file('/etc/sudoers.d/010_orange-nopasswd')
    assert f.is_file
    assert f.exists
    assert f.contains('orange ALL=(ALL) NOPASSWD: ALL')
