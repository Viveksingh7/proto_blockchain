# proto_blockchain

__This repository is dedicated to the concepts of blockchain using python. Since python is one of the most abundant language for programming right now. Hereby I am creating a repo and initializing it with basic concepts for now.__
  
## <u>Updates and fixes :</u>

### Update 1.1 :

><u>__Fixed the mine_block function__</u>
: Error was due to the usage of different spelling for the key "recipient". Due to that the already created chain was not being verified hence no adding of new block.

><u>__Added the string formatter:__</u>:
Added it to calculate the balance check upto 10th place of currency. Since it's the most logical thing to do as the value of cryptos are taken seriously in decimals unlike conventional currencies. 

><u>__Added the lambda function:__</u>:
Added the lambda function to reduce the looping through big chains of transactions.

><u>__Added the reduce function:__</u>:
Added reduce function to further reduce the calculation time.


### Update 1.2 :

><u>__SHA-256__</u>:
A hash function is any function that can be used to map data of arbitrary size to data of fixed size¹. Added SHA-256 for the encryption technique previously we were using the basic hashing of our own.

><u>__Proof of Work:__</u>
Added the proof of work system, heavy computation(theoritically) to check the authenticity of the blocks.

