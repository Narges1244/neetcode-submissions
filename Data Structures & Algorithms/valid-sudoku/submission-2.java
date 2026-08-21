class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> cols = null;
        Set<Character> rows = null;

        for(int i=0; i<9; i++){
            cols = new HashSet<>();
            rows = new HashSet<>();
            for(int j=0; j<9;j++){
                char r = board[i][j];
                char c = board[j][i];
                if(r!= '.'){
                    if(rows.contains(r)){
                        return false;
                    }else{
                        rows.add(r);
                    }
                }
                    if(c!='.'){
                        if(cols.contains(c)){
                            return false;
                        }else{
                            cols.add(c);
                        }
                    }


                
            }
        }
        for(int i=0 ; i<9; i=i+3){
            for(int j=0; j<9; j=j+3){
                if (!checkBlock(i,j,board)){
                    return false;
                }
            }
        }
        return true;
        
    }

    public boolean checkBlock(int idxI, int idxJ, char[][] board){
        Set<Character> square = new HashSet<>();
        int rows = idxI+3;
        int columns = idxJ+3;

        for(int i=idxI; i< rows; i++){
            for(int j= idxJ; j<columns;j++){
                if(board[i][j]=='.'){
                    continue;
                }else{
                    if(square.contains(board[i][j])){
                        return false;
                    }else{
                        square.add(board[i][j]);
                    }
                }
            }
        }
        return true;
    }
}
