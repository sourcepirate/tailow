import asyncio
import profile
from tailow.document import Document
from tailow.fields import *
from tailow.connection import Connection
from tailow import pymongo

loop = asyncio.get_event_loop()

conn = Connection.connect("mongodb://localhost:27017", "test", loop=loop)


class SampleDocument(Document):
    a = IntegerField(required=True)

    class Meta:
        indexes = [("a", pymongo.ASCENDING)]


s = SampleDocument()
s.a = 4


async def saveit():
    await s.save()
    print("save complete")
    await s.delete()
    print("delete also complete")


loop.run_until_complete(saveit())


# sample_id = "5b1b6e5422d638f3779dcd01"

# async def deleteit():
#     s = SampleDocument(id=sample_id)
#     await s.delete()
#     print("Deleted....")

# loop.run_until_complete(deleteit())


class Doc2(Document):
    n = ReferenceField(SampleDocument)


async def helloit():
    sdt = SampleDocument()
    sdt.a = 15
    await sdt.save()
    print("Sample document saved")
    dc = Doc2()
    dc.n = sdt
    await dc.save()
    print("Doc2 saved!!")


loop.run_until_complete(helloit())


async def queryAllDoc2():
    results = await Doc2.objects.all()
    for result in results:
        sam = await result.n.get()
        print(sam)


loop.run_until_complete(queryAllDoc2())
