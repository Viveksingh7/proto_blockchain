# proto_blockchain

__This repository is dedicated to the concepts of blockchain using python. Since python is one of the most abundant language for programming right now. Hereby I am creating a repo and initializing it with basic concepts for now.__


## __<u>Updates and fixes :</u>__

### __Update 1.1:__

><u>__Fixed the mine_block function__</u>
: Error was due to the usage of different spelling for the key "recipient". Due to that the already created chain was not being verified hence no adding of new block.

><u>__Added the string formatter:__</u>:
Added it to calculate the balance check upto 10th place of currency. Since it's the most logical thing to do as the value of cryptos are taken seriously in decimals unlike conventional currencies. 

><u>__Added the lambda function:__</u>:
Added the lambda function to reduce the looping through big chains of transactions.

><u>__Added the reduce function:__</u>:
Added reduce function to further reduce the calculation time.


### __Update 1.2:__

><u>__SHA-256__</u>:
A hash function is any function that can be used to map data of arbitrary size to data of fixed size¹. Added SHA-256 for the encryption technique previously we were using the basic hashing of our own.

><u>__Proof of Work:__</u>
Added the proof of work system, heavy computation(theoritically) to check the authenticity of the blocks.

Minor Tweaks:
>Removed the usage of dictionary
>>Added the   __orderedDict__  such that their is not even a single chance of altering of arguments passed. Sometimes to optimize run time, python tweaks the things a little bit and their is slight possiblity that the dict pair gets altered while passing since their are not ordered in any way.

><u>__Small entitites:__</u>
Seprated the hash as hash.py. Objective is to effectively break the complete file into small entitites.

### __Update 2.0:__

><u>__Fixed Problems with the hashing:__</u>
The hashing was being shown invalid due to faulty parsing.

><u>__Fixed Genesis Block Dependency:__</u>
Fixed the loading problem with the genesis block and the sidwise open_transactions. Function load_data lead to error as initially there was no record to maintain.

><u>__Change the digest to `hexdigest` in hashlib:__</u>
Looping over hexdigest was taking infinite time(I waited for atleast 19 minutes) so changing it to hexdigest was a better option since the first two digits were compared.


><u>__'Fixed the `genesis block problem`:__</u>


### __Update 3.0:__

> <u>__Replaced the procedural with object oriented programming:__</u>
Now all the properties of the block are windup under a ```Class Block```.

> <u>__Fixed the JSON serialization problem:__</u>
Some specific objects are json serializable, hence the Class ```Block``` is not serialized by default.

```text
JSON works with the inbuilt datatypes so by using the __dict__ we can convert to the dictionary type from the default class type
```

```text
The reason to use the copy function is that if we directly apply changes to the blocks of blockchain. Hashing of the previous block stored for the previous transactions can change in serialization. Since to save it from changing another copy is made.
```

> <u>

