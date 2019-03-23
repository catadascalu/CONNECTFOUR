'''
Created on Jan 8, 2018

@author: catad
'''
import random



class Square:
    def __init__(self, x, y):
        self._x = x
        self._y = y 
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y 
    
    
class Board:
    def __init__(self):
        self._board = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
        
        
    def checkWinColumn(self):
        for i in range (0, 7):
            b = self._board
            sum = b[0][i]+b[1][i]+b[2][i]+b[3][i]
            sum_1 = b[1][i]+b[2][i]+b[3][i]+b[4][i]
            sum_2 = b[2][i]+b[3][i]+b[4][i]+b[5][i] 
            
            if sum == 4 or sum == -4 or sum_1 == 4 or sum_1 == -4 or sum_2 == 4 or sum_2 == -4:
                return True
            
    def checkWinRow(self):
        
        for i in range(0, 6):
            b = self._board
            sum = b[i][0]+b[i][1]+b[i][2]+b[i][3]
            sum_1 = b[i][1]+b[i][2]+b[i][3]+b[i][4] 
            sum_2 = b[i][2]+b[i][3]+b[i][4]+b[i][5]
            sum_3 = b[i][3]+b[i][4]+b[i][5]+b[i][6]
            
            
            if sum == 4 or sum == -4 or sum_1 == 4 or sum_1 == -4 or sum_2 == 4 or sum_2 == -4 or sum_3 == 4 or sum_3 == -4:
                return True
        return False
    
    def checkWin(self):
        if self.checkWinColumn() == True or self.checkWinRow() == True:
            return True
        return False
    
    def checkDraw(self):
        if self.checkWin() == False:
            for i in self._board:
                if 0 in i:
                    return False
            return True
        return False
    
    def checkForThreeInAColumn(self, i):
        
        b = self._board
        sum = b[0][i]+b[1][i]+b[2][i]
        sum_1 = b[1][i]+b[2][i]+b[3][i]
        sum_2 = b[2][i]+b[3][i]+b[4][i]
        sum_3 = b[3][i]+b[4][i]+b[5][i]
        
            
          
        if sum == 3:
        
            return 2
        if sum_1 == 3:
            
            return 3
        if sum_2 == 3:
            
            return 4
        if sum_3 == 3:
            
            return 5
            
        return 0
            
    def checkForThreeInARow(self, i):
            
        
        b = self._board
        sum = b[i][0]+b[i][1]+b[i][2]
        sum_1 = b[i][1]+b[i][2]+b[i][3]
        sum_2 = b[i][2]+b[i][3]+b[i][4]
        sum_3 = b[i][3]+b[i][4]+b[i][5]
        sum_4 = b[i][4]+b[i][5]+b[i][6]
            
        if sum == 3:
            return 2
        if sum_1 == 3:
            return 3
        if sum_2 == 3:
            return 4
    
        if sum_3 == 3:
            return 5
        if sum_4 == 3:
            return 6
            
            
        return 0
    
    def generalCheckForThreeInAColumn(self):
        
        for i in range(0, 7):
            b = self._board
            sum = b[0][i]+b[1][i]+b[2][i]
            sum_1 = b[1][i]+b[2][i]+b[3][i]
            sum_2 = b[2][i]+b[3][i]+b[4][i]
            sum_3 = b[3][i]+b[4][i]+b[5][i]
        
            
          
            if sum == 3:
                return [2, i]
            if sum_1 == 3:
                return [3, i]
            if sum_2 == 3:
                return [4, i]
            if sum_3 == 3:
                return [5, i]
            
        return [0, 0]
            
    def generalCheckForThreeInARow(self):
            
        for i in range(0, 6):
            b = self._board
            sum = b[i][0]+b[i][1]+b[i][2]
            sum_1 = b[i][1]+b[i][2]+b[i][3]
            sum_2 = b[i][2]+b[i][3]+b[i][4]
            sum_3 = b[i][3]+b[i][4]+b[i][5]
            sum_4 = b[i][4]+b[i][5]+b[i][6]
            
            if sum == 3:
                return [i, 2]
            if sum_1 == 3:
                return [i, 3]
            if sum_2 == 3:
                return [i, 4]
            if sum_3 == 3:
                return [i, 5]
            if sum_4 == 3:
                return [i, 6]
            
            
        return [0, 0]
    
    def checkForBlockedRow(self, i):
        
            b = self._board
            sum = b[i][0]+b[i][1]+b[i][2]+b[i][3]
            sum_1 = b[i][1]+b[i][2]+b[i][3]+b[i][4]
            sum_2 = b[i][2]+b[i][3]+b[i][4]+b[i][5]
            sum_3 = b[i][3]+b[i][4]+b[i][5]+b[i][6]
            
            
            
            if sum == 2 and b[i][0] != 0 and b[i][1] != 0 and b[i][2] != 0 and b[i][3] != 0 :
                return True
            
            if sum_1 == 2 and b[i][1] != 0 and b[i][2] != 0 and b[i][3] != 0 and b[i][4] != 0 :
                return True
            
            if sum_2 == 2 and b[i][2] != 0 and b[i][3] != 0 and b[i][4] != 0 and b[i][5] != 0 :
                return True
            
            if sum_3 == 2 and b[i][3] != 0 and b[i][4] != 0 and b[i][5] != 0 and b[i][6] != 0 :
                return True
            
            
    def checkForBlockedColumn(self, i):
        
            b = self._board
            sum = b[0][i]+b[1][i]+b[2][i]+b[3][i]
            sum_1 = b[1][i]+b[2][i]+b[3][i]+b[4][i]
            sum_2 = b[2][i]+b[3][i]+b[4][i]+b[5][i]
            
            if sum == 2 and b[0][i] != 0 and b[1][i] != 0 and b[2][i] != 0 and b[3][i] != 0:
                return True
            if sum_1 == 2 and b[1][i] != 0 and b[2][i] != 0 and b[3][i] != 0 and b[4][i] != 0:
                return True
            if sum_2 == 2 and b[2][i] != 0 and b[3][i] != 0 and b[4][i] != 0 and b[5][i] != 0:
                return True
            
           
        
            
        
    
    def __str__(self):
        z = ""
        for i in self._board:
            for j in i:
                if j == 1:
                    z+="R"
                elif j == -1:
                    z+="Y"
                else:
                    z+="."
                
            z += "\n"
            
            
        
        return z
    
    
    def move(self, pos, value):
        if pos.get_x() not in [0, 1, 2, 3, 4, 5] or pos.get_y() not in [0, 1, 2, 3, 4, 5, 6]:
            raise Exception("Move outside the board")
        if self._board[pos.get_x()][pos.get_y()] != 0:
            raise Exception("Square taken")
        self._board[pos.get_x()][pos.get_y()] = value
       
    def getValidMoves(self):
        validMoves = []
        board = self._board
        for l in range(0, 6):
            for i in range(0, 7):
                if board[l][i] == 0:
                    validMoves.append(Square(l, i))
        
        return validMoves
    
    
    
class GamePlay:
    def __init__(self):
        self._boardControl = Board()
        
    def checkValidity(self, x, y):
        validMoves = self._boardControl.getValidMoves()
        for v in validMoves:
            if v.get_x() == x and v.get_y() == y:
                return True
        
    def moveUser(self, pos):
        self._boardControl.move(pos, 1)
    
    def moveAI(self):
        validMoves = self._boardControl.getValidMoves()
    
        if self._boardControl.generalCheckForThreeInARow() == [0, 0] and self._boardControl.generalCheckForThreeInAColumn() == [0, 0]:
            pos = random.randint(0, len(validMoves)-1)
            mov = validMoves[pos]
            self._boardControl.move(mov, -1)
        else:
            k = True
            Gcheck = self._boardControl.generalCheckForThreeInARow()
            GcheckC = self._boardControl.generalCheckForThreeInAColumn()
            
            if Gcheck != [0, 0]:
            
                for i in range(0,6):
                    check = self._boardControl.checkForThreeInARow(i)
                    if self._boardControl.checkForBlockedRow(i) == True:
                        continue
                    elif check == 0:
                        continue
                        
                    
                    
                    if � TokeF�&���@	0�����E-����+�< ���                                p ����        +�'���Advapi  �;     �R(
    �      "<     ��L�&u @`1���9<      �`      �`      �`                                             L                 �42��� 62���0��.���0��.���<��.���      (            @��&����             �42���      (                                                                         @@               �             �       �D                                                                          �                                                     62���                                                                                                                                                                                                                                                         a�*���                    ���                                                                                                                                                                                                                                                                                                                                        �-j(���                        @62���        L62���`       X62���       d62���       t62���       �62���       �62���       �62���       �62���       �62���  �    �62���       �62���       �62���       72���       H72���       t72���       �72���       �72���       �72���       �72���       82���                     @                    !                                       P   ^���d��L�)�L!�V�V            �;               !   	         ��vG��3/C�PS�>�M� �}��iW���	         W���=��:��mh.yl^��]Z@��F�C|BT	         �Yye	�z)��Y�ՙ��-�Dڴr�J��0$	         P.� 8�}�:�iov�ܕ��F���o[�4�'	         �w
ҝ�hkU/R�I(��Vo��Wt��DB�2Xz     P   ^���d��L�)�L!�V�V                     �;      !                                       u e �NtFU^N�&���h   ��+���                                �82���                                                                                                                                                       �      :
     ����	���        �3���                        p<2���        ��}.���        Z�    �<2���P<2���             @��*���0;2���                                                                    =2��� =2���                (                                               P=2���P=2���                                                �=2����=2���                        0              �=2���                �                             >2��� >2���          � �        � �     p8�-����       �      �      `?2���`?2���                               �      �.t3���                                                                                          �     �|00����|00��� z00���                �92���:2���:2���@ @     R�3+����|00���                        `?2���`?2���                                                        �3+���                                                                                  �Thre�o ���        �R�< ���   E             �  x       ���.���      ��                     � �    ���.���j��.���       ���4������4���        	m    ���� ��� 0�� ��� ��� ���        	��        {�  ���� ������� ���           @  �    	     ���)     ��� �����4�����4���(��4���(��4���� �.���   
           ���4����Ww2����V�1���@=�1��� �             J     P��4���P��4���"�+	  Hc@; ����@0���a@ImvC�        H=�1���H=�1���    ���4���@=�1���        8'�1���8'�1���   ���4���0'�1���        H=�1���H=�1��� \A����4���@=�1�����53������4������4���    ���4���                        p=�1���p=�1���        � �.���            
                          ؂�4���؂�4�����4�����4���           
X     <h     C�f    &�
                                                     ��(                                                                             �    ��4���        �  Freen�o ���`V�2���P��2���Ђ�3��� �T    Лf1����h�1��� �T                                                                                                                                            ���'���         EvenN�o ���    p       e \         d i s k                       �  s \ �+�< ���               ���4������4���    �l, ReTa��o ���                                                	 MmSW�o ���p�!6�����6���    ��                                �R.���        8                WA���               g�     i   d   	 Ntfx��o ���CX���                             ؋�4���؋�4���       ���4���`��$���                                                                                          H 