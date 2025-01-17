const hre = require("hardhat");

async function main() {
    const Token = await hre.ethers.getContractAt("Token", "0x14043780bD543039dcd27d9dcDEF27Bd11592939");
    const name = await Token.name();
    console.log("Token Name:", name);

    const totalSupply = await Token.totalSupply();
    console.log("Total Supply:", totalSupply.toString());

    const owner = await Token.owner();
    console.log("Owner:", owner);

    const recipient = "0x2953161C2C1c004a4868595e2b1b839c499660e1";
    const transferAmount = 100;
    await Token.transfer(recipient, transferAmount);
    console.log(`Transferred ${transferAmount} tokens to ${recipient}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
