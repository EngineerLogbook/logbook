cp engbook/.env.example engbook/.env

export KEY=`cat /proc/sys/kernel/random/uuid`

# Generate secret key
sed "s/YOUR SECRET_KEY/$KEY/g" engbook/.env -i
