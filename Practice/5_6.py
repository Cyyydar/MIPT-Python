import random


class Player:
    _myNumber: int # Мое число
    _howClose: int = 1e200 # На сколько противник был близок

    def start_game(self, l, r) -> int:
        pass

    def makeTurn(self) -> int: # Виртуальная функция. Делаем ход игрока - пытаемся угадать число противника
        pass

    def getAnswer(self, str): # Получаем ответ от другого игрока
        pass

    def getNumber(self, guessed_num: int) -> str: # Получить обратно число, сравнить с загаданным и вернуть результат сравнения 
        self._howClose = min(abs(self._myNumber - guessed_num), self._howClose)
        if guessed_num == self._myNumber:
            return "Это правильный ответ"
        elif guessed_num > self._myNumber:
            return "Больше"
        elif guessed_num < self._myNumber:
            return "Меньше"
    
    def howClose(self) -> int:
        return self._howClose


class HumanPlayer(Player):
    def start_game(self, l, r) -> int:
        num = int(input(f"Загадайте число для противника от {l} до {r}: "))
        while(not (l <= num <= r)):
            num = int(input(f"Загадайте число для противника от {l} до {r}: "))
        
        self._myNumber = num
        return num
    
    def makeTurn(self) -> int:
        return int(input(f"Угадайте загаданное число: "))
    
    def getAnswer(self, str):
        print(str)
        
        

class dihPlayer(Player):
    l: int
    r: int

    def start_game(self,l, r) -> int:
        self.l = l
        self.r = r
        self._myNumber = random.randint(l, r)
        return self._myNumber

    def makeTurn(self) -> int:
        mid = (self.l + self.r) // 2
        print("DihBot делает предположение: ", mid)
        return mid

    def getAnswer(self, str): 
        mid = (self.l + self.r) // 2
        
        if str == 'Это правильный ответ':
            print('Ваше число -', mid )
        else:
            if str == 'Больше':
                self.r = mid - 1
            else:
                self.l = mid + 1

class randPlayer(Player):
    l: int
    r: int
    def start_game(self,l, r) -> int:
        self.l = l
        self.r = r
        self._myNumber = random.randint(l, r)
        return self._myNumber

    def makeTurn(self) -> int:
        guess = random.randint(self.l, self.r)
        print("RandBot делает предположение: ", guess)
        return guess

class GameManager:
    player1: Player
    player2: Player

    maxTurn = 10
    currentTurn = 0

    # Границы 
    left = 0
    right = 100
    def createGame(self):
        self.left = int(input(f"Укажите левую границу: "))
        self.right = int(input(f"Укажите правую границу: "))
        
        self.maxTurn = int(input(f"Укажите максимальное количество ходов: "))

        print("[1] - bot-bot")
        print("[2] - bot-human")
        num = int(input(f"Выберите Режим: "))
        match num:
            case 1:
                self.__createBotBot()
            case 2:
                self.__createBotHuman()
    
    def __createBotHuman(self):
        print("[1] - Дихотомия")
        print("[2] - Случайный")
        #num = int(input(f"Выберите Противника: "))
        num = 1
        match num:
            case 1:
                self.player2 = dihPlayer()
            case 2:
                self.player2 = randPlayer()
        
        self.player2.start_game(self.left, self.right)


        self.player1 = HumanPlayer()
        print("Вы - Игрок1")
        self.player1.start_game(self.left, self.right)

        self.__gameLoop()

    def __createBotBot(self):
        self.player1 = dihPlayer()
        self.player1.start_game(self.left, self.right)

        self.player2 = randPlayer()
        self.player2.start_game(self.left, self.right)

        self.__gameLoop()

    def __gameLoop(self):
        while self.currentTurn < self.maxTurn:
            print("=" * 10, "Ход", self.currentTurn, "=" * 10)
            print("Ход Игрока1 " + "=" * 10)
            
            result = self.player2.getNumber(self.player1.makeTurn()) # Пытаемся угадать число противника
            if result == "Это правильный ответ":
                self.__endGame(1)
                return
            self.player1.getAnswer(result) # Записываем его себе

            print("Ход Игрока2 " + "=" * 10)

            result = self.player1.getNumber(self.player2.makeTurn())
            if result == "Это правильный ответ":
                self.__endGame(2)
                return
            self.player2.getAnswer(result)

            self.currentTurn += 1
        
        print("Ходы закончились")
        if self.player1.howClose() < self.player2.howClose():
            self.__endGame(1)
        else:
            self.__endGame(2)
            

    def __endGame(self, winner):
        print("Победил игрок", winner, "за", self.currentTurn, "хода(ов)")
            


gameMaster = GameManager()
gameMaster.createGame()