# proto_blockchain

__This repository is dedicated to the concepts of blockchain using python. Since python is one of the most abundant language for programming right now. Hereby I am creating a repo and initializing it with basic concepts for now.__

## Functions for now:

* ### get_transaction_value
  __This function is going to input two value for now that is `recipient` and `amount`. Sender is automatically John Doe for now.__
  
* ### add_transaction
  __Appends the last_value and new_value to the open_transaction(sidewise).__
  
* ### mine_block:
  __function to add new blocks to the chain `open_blockchain`__

* ### hack_blockchain:
  __<em>this function is created to show the problems with the lists data type usage in making of blocks. `Lists are mutable hence they can be altered.` To avoid this we have created a reverse checker such that it verifies each and every block from the start. </em>__

``` .{line-numbers}
1. The hack function is going to only alter the first block i.e. `genenis_block`.
2. When it will alter it, the validation will run itself against the blocks and noitce the anomaly.
3. It won't let the data go into system as the anomaly is detected.
```
  
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

