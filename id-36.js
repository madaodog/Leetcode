/**
 * 36. Valid Sudoku
 * Source: https://leetcode.com/problems/valid-sudoku/
 */


/**
Shitty solution
 */
const isValidSudoku = (board) => {

    // row can be fed directly into isValid
    for(let i = 0; i < board.length; i++) {
        if(!isUnique(board[i])) {
            return false;
        }
        if(!isUnique(mapToColumn(board, i))) {
            return false;
        }
        if(i % 3 === 1) {
            if(!mapToCube(board, i)) {
                return false;
            }
        }
    }
    return true;
}

const mapToColumn = (board, i) => {
    return board.map((element => element[i]));
}

const mapToCube = (board, i) => {
    // first cube
    const firstCube = [...board.map((element) => element[i-1]).slice(0, 3),
    ...board.map((element) => element[i]).slice(0,3),
    ...board.map((element) => element[i+1]).slice(0,3)]

    // second cube
    const secondCube = [...board.map((element) => element[i-1]).slice(3, 6),
    ...board.map((element) => element[i]).slice(3,6),
    ...board.map((element) => element[i+1]).slice(3,6)]

    // third cube
    const thirdCube = [...board.map((element) => element[i-1]).slice(6, 9),
    ...board.map((element) => element[i]).slice(6,9),
    ...board.map((element) => element[i+1]).slice(6,9)]

    return isUnique(firstCube) && isUnique(secondCube) && isUnique(thirdCube);
}

const isUnique = (row) => {
    const nodots = row.filter(element => element !== ".");
    const uniqueRow = new Set(nodots);
    if(uniqueRow.size === nodots.length) {
        return true;
    }
    return false;
}
