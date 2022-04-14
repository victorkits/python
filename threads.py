# Concurrency (paralelism)
# look for aiohttp


from multiprocessing import Process
import asyncio


async def my_corutine():
    return "Hello"


def squad(a):
    print(a**2)
    # return a ** 2


async def find_divisibles(inrange, div_by): # Notify the python that this finction whill be running async
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    # This block of code whill be running sync
    # divs1 = find_divisibles(50899000, 125) # whil be calculated during x seconds or hours
    # divs2 = find_divisibles(508000, 11235)
    # divs3 = find_divisibles(508000, 134)

    divs1 = loop.create_task(find_divisibles(50899000, 125))
    divs2 = loop.create_task(find_divisibles(508000, 11235))
    divs3 = loop.create_task(find_divisibles(508000, 134))
    await asyncio.wait([divs1, divs2, divs3])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()





    # c = my_corutine()
    # loop = asyncio.get_event_loop()
    # loop.
    # res = loop.run_until_complete(c)
    # print(res)

    # arr = [1, 2, 3, 4, 5]
    # for a in arr:
    #     process = Process(target=squad, args=(a,))
    #     process.name = str(a)
    #     # print(process.__dir__())
    #     print(f'process.name is: {process.name}')
    #     process.start()

