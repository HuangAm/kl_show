#!/bin/bash
name=license
password=V5RFzoJcmu5UDGnZD3wy8SG3kIgpXGiCYRfGqmwpFYtL1kkFVO0X7pH-9o2GnIfku2WTitukzOjJFjcdCTX0ULB7V2nQcgVDd4514-kdhK0zD2cMZ-cBMW8hEaV5BLk9dtt6VKSndNDb12Vuud1k7THXeWv-xB8ypRGAQEbUbt0=C8gKl7xPEXFJT-hWNtOplG_gbCeVoFqgk5Fp4G3Nzjc0z5Xrz6B_A0DZXPsEaBJcnTfb09SdJki58LG_jP4YK2wOPMjWKcO9ZzHYBR5E_eZWcvMnBlyKhmKctonOxZAB4tW0bi85rIyAH-JRge49wY1yu0x7AnPBnHggp_tiymU=
host=rqdatad-pro.ricequant.com
port=16011
url=rqdata://${name}:${password}@${host}:${port}
echo "export RQDATAC2_CONF=$url" >> ~/.bash_profile
source ~/.bash_profile
