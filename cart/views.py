from django.shortcuts import render, redirect, get_object_or_404
from .models import Competition, Cart, CartItem
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from random import choice

def _cart_id(request):
   cart = request.session.session_key
   if not cart:
      cart = request.session.create()
   return cart 

# def add_cart(request, competition_id):
#    question_answer = request.POST['question_answer']
#    quantity = request.POST['quantity']
#    competition = Competition.objects.get(id=competition_id)
#    if question_answer == "Choose an Option":
#       messages.error(request, f"You must answer the question to proceed.")
#       return redirect('../../competitions/' + str(competition.slug))
#    try:
#       cart = Cart.objects.get(cart_id=_cart_id(request))
#    except Cart.DoesNotExist:
#       cart = Cart.objects.create(
#             cart_id = _cart_id(request)
#          )
#       cart.save(),
#    try:
#       cart_item = CartItem.objects.get(competition=competition, cart=cart)
#       if cart_item.quantity <= cart_item.competition.tickets_remaining:
#          cart_item.quantity += int(quantity)
#          # cart_item.competition.tickets_remaining -= 1
#       cart.save()
#    except CartItem.DoesNotExist:
#       cart_item = CartItem.objects.create(
#          competition = competition,
#          quantity = quantity,
#          cart = cart
#          )
#       if cart_item.competition.tickets_remaining < int(quantity):
#          # Delete the cart item
#          cart_item.delete()
#          # Print error message on competitions page and redirect
#          messages.error(request, f"There are only {cart_item.competition.tickets_remaining}  tickets left in this competition")
#          return redirect('../../competitions/' + str(competition.slug))
#       else:
#          # If there are more tickets left than quantity 
#          # Tickets_remaining - quantity
#          print('testing')
#          # cart_item.competition.tickets_remaining -= int(quantity)
#       cart_item.save()
#    return redirect('cart:cart_detail')

# def add_cart(request, competition_id):
#    question_answer = request.POST['question_answer']
#    quantity = request.POST['quantity']
#    competition = Competition.objects.get(id=competition_id)
#    # Making sure that question is answered
#    if question_answer == "Choose an Option":
#       messages.error(request, f"You must answer the question to proceed.")
#       return redirect('../../competitions/' + str(competition.slug))
#    # Making sure that quantity is not set to 0
#    if quantity == '0':
#       messages.error(request, f"You must enter a quantity of tickets.")
#       return redirect('../../competitions/' + str(competition.slug))
#    # Check if user is authenticated
#    if request.user.is_authenticated:
#       # If there is no cart - create one
#       try:
#          cart = Cart.objects.get(cart_id=_cart_id(request))
#       except Cart.DoesNotExist:
#          cart = Cart.objects.create(
#                cart_id = _cart_id(request)
#             )
#          cart.save(),
#       try:
#          # If there is a cart item - add the quantity of the selected competition ticket to it
#          cart_item = CartItem.objects.get(competition=competition, cart=cart)
#          ticket_numbers = cart_item.ticket_numbers
#          if cart_item.quantity < (cart_item.competition.number_of_tickets - cart_item.competition.tickets_sold):
#             cart_item.quantity += int(quantity)
#             for x in quantity:
#                ticket_numbers.append(choice(competition.ticket_array))
#             # print(CartItem.ticket_numbers[1])
#             print(ticket_numbers)
#          # Will need to add steps to ensure that a particular user cannot have more than 5/10 tickets
#          # per specific competition 
#          cart_item.save()
#       # If the cart does not exist - create it with the details from the competition 
#       except CartItem.DoesNotExist:
#             # ticket_number = choice(competition.ticket_array)
#             ticket_numbers = []
#             for x in range(int(quantity)):
#                ticket_numbers.append(choice(competition.ticket_array))
#             cart_item = CartItem.objects.create(
#                competition = competition,
#                quantity = quantity,
#                cart = cart,
#                ticket_numbers = ticket_numbers
#                )
#             print(ticket_numbers)
#             if int(quantity) > (cart_item.competition.number_of_tickets - cart_item.competition.tickets_sold):
#                cart_item.delete()
#                # Print error message on screen
#                messages.error(request, f"There are only {cart_item.competition.number_of_tickets - cart_item.competition.tickets_sold} tickets remaining.")
#                return redirect('../../competitions/' + str(competition.slug))
#             else:
#                cart_item.save()
#                # print(Competition.ticket_array.pop(0))
#                # arr = []
#                # for num in Competition.ticket_array:
#                #    arr.push(num)
#                # print(arr)
#       return redirect('cart:cart_detail')
#    # If user is not authenticated - redirect to the page and ask them to log in 
#    else: 
#       messages.error(request, "You must be logged into add to the cart")
#       return redirect('../../competitions/' + str(competition.slug))



def add_cart(request, competition_id):
   question_answer = request.POST['question_answer']
   quantity = request.POST['quantity']
   competition = Competition.objects.get(id=competition_id)
   # Making sure that question is answered
   if question_answer == "Choose an Option":
      messages.error(request, f"You must answer the question to proceed.")
      return redirect('../../competitions/' + str(competition.slug))
   # Making sure that quantity is not set to 0
   if quantity == '0':
      messages.error(request, f"You must enter a quantity of tickets.")
      return redirect('../../competitions/' + str(competition.slug))
   # Check if user is authenticated
   if request.user.is_authenticated:
      # If there is no cart - create one
      try:
         cart = Cart.objects.get(cart_id=_cart_id(request))
      except Cart.DoesNotExist:
         cart = Cart.objects.create(
               cart_id = _cart_id(request)
            )
         cart.save(),
      try:
         # If there is a cart item - add the quantity of the selected competition ticket to it
         cart_item = CartItem.objects.get(competition=competition, cart=cart)
         ticket_numbers = cart_item.ticket_numbers
         if cart_item.quantity < (cart_item.competition.number_of_tickets - cart_item.competition.tickets_sold):
            cart_item.quantity += int(quantity)
            for x in range(0, int(quantity)):
               new_ticket_number = choice(competition.ticket_array)
               while True: 
                  if new_ticket_number in ticket_numbers:
                     new_ticket_number = choice(competition.ticket_array)
                  else: 
                     ticket_numbers.append(new_ticket_number)
                     break
               # ticket_numbers.append(choice(competition.ticket_array))
            # print(CartItem.ticket_numbers[1])
         # Will need to add steps to ensure that a particular user cannot have more than 5/10 tickets
         # per specific competition 
         cart_item.save()
      # If the cart does not exist - create it with the details from the competition 
      except CartItem.DoesNotExist:
            # ticket_number = choice(competition.ticket_array)
            ticket_numbers = []
            for x in range(int(quantity)):
               # ticket_numbers.append(choice(competition.ticket_array))
               new_ticket_number = choice(competition.ticket_array)
               while True: 
                  if new_ticket_number in ticket_numbers:
                     new_ticket_number = choice(competition.ticket_array)
                  else: 
                     ticket_numbers.append(new_ticket_number)
                     break
            cart_item = CartItem.objects.create(
               competition = competition,
               quantity = quantity,
               cart = cart,
               ticket_numbers = ticket_numbers
               )
            if int(quantity) > (cart_item.competition.number_of_tickets - cart_item.competition.tickets_sold):
               cart_item.delete()
               # Print error message on screen
               messages.error(request, f"There are only {cart_item.competition.number_of_tickets - cart_item.competition.tickets_sold} tickets remaining.")
               return redirect('../../competitions/' + str(competition.slug))
            else:
               cart_item.save()
               # print(Competition.ticket_array.pop(0))
               # arr = []
               # for num in Competition.ticket_array:
               #    arr.push(num)
               # print(arr)
      return redirect('cart:cart_detail')
   # If user is not authenticated - redirect to the page and ask them to log in 
   else: 
      messages.error(request, "You must be logged into add to the cart")
      return redirect('../../competitions/' + str(competition.slug))


def cart_detail(request, total=0, counter=0, cart_items=None):
   try:
      cart = Cart.objects.get(cart_id=_cart_id(request))
      cart_items = CartItem.objects.filter(cart=cart, active=True)
      for cart_item in cart_items:
         if cart_item.competition.sale_ticket_price:
            total += (cart_item.competition.sale_ticket_price * cart_item.quantity)
         else:
            total += (cart_item.competition.price_of_ticket * cart_item.quantity)
         counter += cart_item.quantity
   except ObjectDoesNotExist:
      pass
   
   return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def plus_icon(request, competition_id):
   cart = Cart.objects.get(cart_id=_cart_id(request))
   competition = get_object_or_404(Competition, id=competition_id)
   cart_item = CartItem.objects.get(competition=competition, cart=cart)
   ticket_numbers = cart_item.ticket_numbers
   if cart_item.quantity < (cart_item.competition.number_of_tickets - cart_item.competition.tickets_sold):
      cart_item.quantity = cart_item.quantity + 1
      # ticket_numbers.append(choice(competition.ticket_array))
      new_ticket_number = choice(competition.ticket_array)
      # while new_ticket_number not in ticket_numbers:
      #    ticket_numbers.append(new_ticket_number)
      # else: 
      #     new_ticket_number = choice(competition.ticket_array)
      while True:
         if new_ticket_number in ticket_numbers:
            new_ticket_number = choice(competition.ticket_array)
         else:
            ticket_numbers.append(new_ticket_number)
            break
      cart_item.save()
   else:
      messages.error(request, 'There are no tickets left for this competition')
   return redirect('cart:cart_detail')

# Test function with test button to remove the item from the array (once purchased)
def remove_from_ticket_array(request, competition_id):
   cart = Cart.objects.get(cart_id=_cart_id(request))
   competition = get_object_or_404(Competition, id=competition_id)
   try:
      cart_item = CartItem.objects.get(competition=competition, cart=cart)
   except:
      pass
   ticket_numbers = cart_item.ticket_numbers
   ticket_number = 1
   competition.ticket_array.remove(ticket_number)
   competition.tickets_sold += 1
   competition.save()
   return redirect('cart:cart_detail')


def cart_remove(request, competition_id):
   cart = Cart.objects.get(cart_id=_cart_id(request))
   competition = get_object_or_404(Competition, id=competition_id)
   cart_item = CartItem.objects.get(competition=competition, cart=cart)
   ticket_numbers = cart_item.ticket_numbers
   if cart_item.quantity > 1:
      cart_item.quantity = cart_item.quantity - 1
      ticket_numbers.pop()
      cart_item.save()
   else:
      cart_item.delete()
   return redirect('cart:cart_detail')

def full_remove(request, competition_id):
   cart = Cart.objects.get(cart_id=_cart_id(request))
   competition = get_object_or_404(Competition, id=competition_id)
   cart_item = CartItem.objects.get(competition=competition, cart=cart)
   cart_item.delete()
   return redirect('cart:cart_detail')