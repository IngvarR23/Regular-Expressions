from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  new_list = []

def formatting_name():
   for n in contacts_list:
      s1 = ' '.join(n[:3])
      if s1.strip().count(' ') == 1:
         contacts_list[contacts_list.index(n)] = s1.split() + n[2:]
      else:
         contacts_list[contacts_list.index(n)] = s1.split() + n[3:]
   
   return 
   
def formatting_number():
   for u in contacts_list:
      pattern1 = r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?'
      u[5] = re.sub(pattern1, r'+7(\2)\3-\4-\5\7\8\9', u[5])
   return
   

def unite_all():
   for n in range(1, len(contacts_list)):
      for u in range(1, len(contacts_list)):
         if contacts_list[n][:2] == contacts_list[u][:2]:
            for c in range(len(contacts_list[0])):
               if contacts_list[n][c] == '': 
                  contacts_list[n][c] = contacts_list[u][c]
               
   
   for d in contacts_list:
      if len(d) == len(contacts_list[0]) and d not in new_list:
         new_list.append(d)
   return        
         
         


                

		

if __name__ == '__main__':
   formatting_name()
   formatting_number()
   unite_all()
   pprint(new_list)
   with open("phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_list)