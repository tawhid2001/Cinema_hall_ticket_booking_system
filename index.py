class Star_cinema:
    hall_list = []

    def entry_hall(self,hall):
        self.hall_list.append(hall)



class Hall(Star_cinema):
    
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.__allocate_seats()
    
    def __allocate_seats(self):
        matrix = [[0]*self.cols for _ in range(self.rows)]

        self.seats[self.hall_no] = matrix


    def entry_show(self,id,movie_name,time):
        self.show_list.append((id,movie_name,time))

    def book_seats(self,id,seats_to_book):
        show = None
        for s in self.show_list:
            if s[0] == id:
                show = s
                break

        if show:
            matrix = self.seats[self.hall_no]
            for seat in seats_to_book:
                row, col = seat
                if (0<=row and row < self.rows) and (0<=col and col<self.cols):
                    if matrix[row][col] == 0:
                        matrix[row][col] = 1
                    else:
                        print(f"Seat ({row},{col} is already booked.)")
                else:
                    print(f"Seat ({row},{col} does not exist)")

            print("Seats Succusfully Booked Matrix:")
            for row in matrix:
                print(row)
            
        else:
            print(f"Show with id {id} not found")


    def view_show_list(self):
        string =f"Hall Number: {self.hall_no}\n"
        for show in self.show_list:
            string +=f"ID: {show[0]} Movie Name: {show[1]} Time: {show[2]}\n"
        
        return string

        
        

    def view_available_seats(self,id):

        show = None
        for s in self.show_list:
            if s[0] == id:
                show = s
                break

        if show:
            matrix = self.seats[self.hall_no]

            for row in range(self.rows):
                for col in range(self.cols):
                    if matrix[row][col] == 0:
                        print(f"({row},{col})")
        else:
            print(f"Show with ID: {id} does not exist")





hall1 = Hall(5, 5, 1)
hall2 = Hall(5, 5, 2)
hall3 = Hall(5, 5, 3)
hall4 = Hall(5, 5, 4)

st = Star_cinema()

st.entry_hall(hall1)
st.entry_hall(hall2)
st.entry_hall(hall3)
st.entry_hall(hall4)


hall1.entry_show(1, "Devdas", "12:00 PM")
hall1.entry_show(2, "Main Hu na", "3:00 PM")

hall2.entry_show(3, "Jawan", "3:00 PM")
hall2.entry_show(4, "Kung fu panda", "12:00 PM")

hall3.entry_show(5, "Dunki", "12:00 PM")
hall3.entry_show(6, "Spider-Man", "3:00 PM")

hall4.entry_show(7, "Harry Potter", "12:00 PM")
hall4.entry_show(8, "Surongo", "3:00 PM")


run = True

while run:

    print("1. View All Show Today")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")

    op = int(input("\n\tEnter Option: "))

    if op == 1:
        for hall in st.hall_list:
            print(hall.view_show_list())


    if op == 2:
        hall_num = int(input("\n\tEnter Hall Number: "))
    
        for hall in st.hall_list:
            if hall.hall_no == hall_num:
                print("\n\tAvailable Shows:")
                print(hall.view_show_list())
                show_id = int(input("\n\tEnter Show ID: "))
                hall.view_available_seats(show_id)
                break
        else:
            print("Invalid Hall Number")

    if op == 3:
        hall_num = int(input("\n\tEnter Hall Number: "))
        valid_hall = False
        for hall in st.hall_list:
            if hall.hall_no == hall_num:
                valid_hall = True
                print("\n\tAvailable Shows:")
                print(hall.view_show_list())
                show_id = int(input("\n\tEnter Show ID: "))
                for show in hall.show_list:
                    if show[0] == show_id:
                        how_many = int(input("How many seats: "))
                        seats_to_book = []
                        for _ in range(how_many):
                            row = int(input("Enter Row Number: "))
                            col = int(input("Enter Col Number: "))
                            seats_to_book.append((row, col))
                        hall.book_seats(show_id, seats_to_book)

                        break  
                    else:
                        print("Invalid ID")
                        break  

        if not valid_hall:
            print("Invalid Hall Number")

    if op == 4:
        run = False

        

        



        

