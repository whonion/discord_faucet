#create wallets
for i in {1..161}; do <tendermit-d> keys add ML$i; done && \
#transfer of tokens to the main address
for i in {1..161}; do <tendermit-d> tx bank send ML$i <your_address> 9960000uatom --fees 500uatom -y;done
