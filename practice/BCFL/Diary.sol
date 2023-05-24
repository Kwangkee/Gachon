pragma solidity ^0.8.6;

contract Diary {
    // date => string
    address internal owner;
    mapping(uint256 => string) public diary;

    constructor() public {
        owner = msg.sender;
    }

    function getNumberlength (uint256 number) public pure returns(uint ){
        uint digits;
        while(number >0){
            number /= 10;
            digits++;
        }
        return digits;
    }

    function addDiary(uint256 date, string memory content) public {
        require(msg.sender == owner,"Only owner of this contract can edit diary");
        require(getNumberlength(date) == 8,"Enter date in YYYYMMDD format");
        diary[date] = content;
    }

    function readDiary(uint256 date) public view returns (string memory) {
        require(msg.sender == owner, "Only owner of this contract can read diary");
        require(getNumberlength(date) == 8,"Enter date in YYYYMMDD format");
        return diary[date];
    }


}
