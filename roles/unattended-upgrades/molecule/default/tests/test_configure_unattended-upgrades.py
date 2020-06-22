import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_unattended_upgrades_configuration(host):
    f = host.file("/etc/apt/apt.conf.d/50unattended-upgrades")
    assert f.exists
    assert f.contains('"origin=Debian,codename=${distro_codename},label=Debian-Security";')
    assert f.contains('Unattended-Upgrade::AutoFixInterruptedDpkg "true";')
    assert f.contains('Unattended-Upgrade::InstallOnShutdown "false";')
    assert f.contains('Unattended-Upgrade::Remove-Unused-Dependencies "true";')
    assert f.contains('Unattended-Upgrade::Automatic-Reboot "true";')
    assert f.contains('Unattended-Upgrade::Automatic-Reboot-WithUsers "true";')
    assert f.contains('Unattended-Upgrade::Automatic-Reboot-Time "02:00";')

    f = host.file("/etc/apt/apt.conf.d/20auto-upgrades")
    assert f.exists
    assert f.contains('APT::Periodic::Enable "1"')
    assert f.contains('APT::Periodic::Unattended-Upgrade "1";')
    assert f.contains('APT::Periodic::Update-Package-Lists "1";')
    assert f.contains('APT::Periodic::Download-Upgradeable-Packages "1";')
    assert f.contains('APT::Periodic::AutocleanInterval "7";')
