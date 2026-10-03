import shutil
from preset import cutscenes as cs
from preset import utils as u

def welc_asc():
	u.clear()
	u.v_fast_print(r"""
			,-.-.     ,----.              _,.----.     _,.---._           ___      ,----.  
	,-..-.-./  \==\ ,-.--` , \   _.-.    .' .' -   \  ,-.' , -  `.  .-._ .'=.'\  ,-.--` , \ 
	|, \=/\=|- |==||==|-  _.-` .-,.'|   /==/  ,  ,-' /==/_,  ,  - \/==/ \|==|  ||==|-  _.-` 
	|- |/ |/ , /==/|==|   `.-.|==|, |   |==|-   |  .|==|   .=.     |==|,|  / - ||==|   `.-. 
	\, ,     _|==/==/_ ,    /|==|- |   |==|_   `-' \==|_ : ;=:  - |==|  \/  , /==/_ ,    / 
	| -  -  , |==|==|    .-' |==|, |   |==|   _  , |==| , '='     |==|- ,   _ |==|    .-'  
	\  ,  - /==/|==|_  ,`-._|==|- `-._\==\.       /\==\ -    ,_ /|==| _ /\   |==|_  ,`-._ 
	|-  /\ /==/ /==/ ,     //==/ - , ,/`-.`.___.-'  '.='. -   .' /==/  / / , /==/ ,     / 
	`--`  `--`  `--`-----`` `--`-----'                `--`--''   `--`./  `--``--`-----``  
""")

def welc_text():
	width = shutil.get_terminal_size().columns

	u.slow_print(f"{'Welcome to the amazing digital world!':^{width}}")
	u.slow_print(f"{'You will live as a stranded person in a camp alone... for now!':^{width}}")
	u.slow_print("")
	u.v_fast_print(f"{'Please Choose One of The Options.':^{width}}")
	u.v_fast_print(f"{'1. START':^{width}}")
	u.v_fast_print(f"{'2. QUIT ':^{width}}")

	x = u.getch()

	if x == "1":
		cs.start()
		return True
	elif x == "2":
		return False



def bye_asc():
	u.clear()
	u.v_fast_print(r"""
        ,----,                                                              
      ,/   .`|       ,--,                        ,--.       ,--.            
    ,`   .'  :     ,--.'|   ,---,              ,--.'|   ,--/  /| .--.--.    
  ;    ;     /  ,--,  | :  '  .' \         ,--,:  : |,---,': / '/  /    '.  
.'___,/    ,',---.'|  : ' /  ;    '.    ,`--.'`|  ' ::   : '/ /|  :  /`. /  
|    :     | |   | : _' |:  :       \   |   :  :  | ||   '   , ;  |  |--`   
;    |.';  ; :   : |.'  |:  |   /\   \  :   |   \ | :'   |  /  |  :  ;_     
`----'  |  | |   ' '  ; :|  :  ' ;.   : |   : '  '; ||   ;  ;   \  \    `.  
    '   :  ; '   |  .'. ||  |  ;/  \   \'   ' ;.    ;:   '   \   `----.   \ 
    |   |  ' |   | :  | ''  :  | \  \ ,'|   | | \   ||   |    '  __ \  \  | 
    '   :  | '   : |  : ;|  |  '  '--'  '   : |  ; .''   : |.  \/  /`--'  / 
    ;   |.'  |   | '  ,/ |  :  :        |   | '`--'  |   | '_\.'--'.     /  
    '---'    ;   : ;--'  |  | ,'        '   : |      '   : |     `--'---'   
             |   ,/      `--''          ;   |.'      ;   |,'                
             '---'                      '---'        '---'                  
""")

def bye_text():
	width = shutil.get_terminal_size().columns
	u.slow_print(f"{'Thank You for playing my game!':^{width}}")
	u.slow_print(f"{'Your Playtime is very much appreciated!':^{width}}")
	u.slow_print(f"{'See you next time, player!':^{width}}")


#	slow_print(f"{'':^{width}}")
# 	fast_print(f"{'':^{width}}")

if __name__ == "__main__":
	bye_asc()
	bye_text()