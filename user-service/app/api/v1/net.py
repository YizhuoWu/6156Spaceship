import aiohttp


async def validate_address(street, stree2, city, state, zipcode=""):
    async with aiohttp.ClientSession() as session:
        body = {"street": street, "street2": stree2, "city": city, "state": state, "zipcode": zipcode}
        async with session.get(
                'http://addrvalidationservice-env.eba-jtfahpj7.us-east-1.elasticbeanstalk.com/validate?',
                json=body) as response:
            return await response.text()
