# Requirements
- python 3
- MySQL
- GeoIP
- twisted

# Installation

Python 3 is required before proceeding to next steps.

```
# git clone git@github.com:spring/uberserver.git
# python3 -m venv ~/var/www/.virtualenvs/uberserver
# source ~/virtenvs/uberserver/bin/activate
# pip install SQLAlchemy pycrypto twisted pyOpenSSL GeoIP mysqlclient
```

Note: The last command mail fail if you don't have MySQL or GeoIP installed,
you can omit these as they aren't required for testing purposes.

Without further configuration this will create a SQLite database (server.db).
Performance will be OK for testing and small setups. For production use,
setup MySQL/PostgreSQL/etc.


## Installing and configuring GeoIP


1. First create the GeoIP directory

        sudo mkdir /usr/local/share/GeoIP

2. Now, move the GeoLite City binary database to it's new location.

        sudo mv geoip/GeoLiteCity.dat /usr/local/share/GeoIP/

3. Install the GeoIP C Library

        cd geoip/GeoIP-1.4.8

4. Now, configure and install the GeoIP C library by issuing the following commands.

        ./configure
        make
        make check
        sudo make install


# Usage

    source ~/var/www/.virtualenvs/uberserver/bin/activate
    ./server.py -v 103.0

For more information:

    ./server.py --help

# Logs
- `$PWD/server.log`
