GDK-PixBuf / shared-mime-info bug
=================================

This repository is a minimal test case for a bug discovered in the
Ubuntu 12.04 packaging of `libgdk-pixbuf2.0-0`.

It's a virtual machine package based on the Vagrant Ubuntu 12.04
base box (`precise64`).

Refs: https://bugs.launchpad.net/ubuntu/+source/gdk-pixbuf/+bug/1032849

Requirements
------------

* Vagrant (http://www.vagrantup.com/)
* Fabric (http://www.fabfile.org/)

Instructions
------------

All commands should be run in the host machine.

1. `vagrant up` -- if you don't have the `precise64` base box, this will take a while.
2. `fab provision` -- installs the base packages required to build `test.c`.
3. `fab test` -- this is expected to fail with an "Error Unrecognized image file format".
4. `fab fix_things` -- this installs `shared-mime-info`.
5. `fab test` -- this is expected not to fail anymore and output "Image size: (X x Y)".
6. `vagrant destroy` -- get rid of the virtual machine.
