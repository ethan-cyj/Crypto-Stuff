//SPDX-License-Identifier: UNLICENSED

// Solidity files have to start with this pragma.
pragma solidity ^0.8.0;


contract Token {
    string public name = "Ethan Token";
    string public symbol = "ETHT";
    uint256 public totalSupply = 1000000;
    address public owner;
    mapping(address => uint256) balances;

    // The Transfer event helps off-chain applications understand what happens within your contract.
    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    constructor() {
        // The totalSupply is assigned to the transaction sender, which is the
        // account that is deploying the contract.
        balances[msg.sender] = totalSupply;
        owner = msg.sender;
    }

    /**
     * A function to transfer tokens.
     *
     * The `external` modifier makes a function *only* callable from *outside*
     * the contract.
     */
    function transfer(address to, uint256 amount) external {
        // Check if the transaction sender has enough tokens.
        // If `require`'s first argument evaluates to `false`, the
        // transaction will revert.
        require(balances[msg.sender] >= amount, "Not enough tokens");
        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
    }

    /**
     * Read only function to retrieve the token balance of a given account.
     *
     * The `view` modifier indicates that it doesn't modify the contract's
     * state, which allows us to call it without executing a transaction.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}