class Student:

    extension_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_extension_days(self, student, days):
        student.extension_days = days
        
        
class Email:
    """
    Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    >>> email = Email('hello', 'Alice', 'Bob')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Alice'
    >>> email.recipient_name
    'Bob'
    """
    def __init__(self, msg, sender_name, recipient_name):
        "*** YOUR CODE HERE ***"
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        
class Client:
    """
    Every Client has three instance attributes: name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """
    def __init__(self, server, name):
        self.inbox = []
        "*** YOUR CODE HERE ***"
        self.server = server
        self.name = name
        self.serve.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        "*** YOUR CODE HERE ***"
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)


    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        "*** YOUR CODE HERE ***"
        self.inbox.append(email)


class Server:
    """
    Each Server has one instance attribute: clients (which
    is a dictionary that associates client names with
    client objects).
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """
        Take an email and put it in the inbox of the client
        it is addressed to.
        """
        "*** YOUR CODE HERE ***"
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        """
        Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        "*** YOUR CODE HERE ***"
        self.client[client_name] = client



class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard stores an arbitrary number of Buttons in a dictionary. 
    Each dictionary key is a Button's position, and each dictionary
    value is the corresponding Button.
    >>> b1, b2 = Button(5, "H"), Button(7, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[5].key
    'H'
    >>> k.press(7)
    'I'
    >>> k.press(0) # No button at this position
    ''
    >>> k.typing([5, 7])
    'HI'
    >>> k.typing([7, 5])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for button in args:
            self.buttons[button.pos] = button

    def press(self, pos):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if pos in self.buttons.keys():
            b = self.buttons[pos]
            b.times_pressed += 1
            return b.key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        accumulate = ''
        for pos in typing_input:
            accumulate += self.press(pos)
        return accumulate

class Butterfly():
    def __init__(self, wings=2):
        self.wings = wings

class Monarch(Butterfly):
    def __init__(self):
        super().__init__()
        self.colors = ['orange', 'black', 'white']

class MimicButterfly(Butterfly):
    def __init__(self, mimic_animal):
        super().__init__()
        self.mimic_animal = mimic_animal



class Pet():

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)
        
           
              
class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + ' says meow!')
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.live > 0:
            self.live -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("This cat has no more lives to lose.")
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name}, {self.lives} lives"
         
    def revive(self):
        """Revives a cat from the dead. The cat should now have 
        9 lives and is_alive should be true. Can only be called
        on a cat that is dead. If the cat isn't dead, print 
        'This cat still has lives to lose.'
        """
        if not self.is_alive:
            self.__init__(self.name, self.owner)
        else:
            print('This cat still has lives to lose')



class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"
        super.__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk(self)
        super().talk(self)

class Car:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
         return self.color

    def __str__(self):
         return self.color * 2

class Garage:
    def __init__(self):
         print('Vroom!')
         self.cars = []

    def add_car(self, car):
         self.cars.append(car)

    def __repr__(self):
         print(len(self.cars))
         ret = ''
         for car in self.cars:
             ret += str(car)
         return ret