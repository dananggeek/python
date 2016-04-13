list1 , list2= [123,'qwe','qwerty',12,'a'],[678,'hgr'];
list3=list2+[999];
list4 =['ini','ini',123];
aList =[123, 'xyz', 'zara', 'abc', 123];

print cmp(list1,list2);
print cmp(list2,list1);
print list3;
print cmp(list2,list3);
print  "firts list lemght", len(list1);
print  "second list lenght", len (list2)
print "Max value ",max(list1);
print "minimal list ",min(list1);
list2.append('tambah');
print "menambah data list2 dengan nama tambah pada list2",list2;
print "menambah data list2 dengan nama tambah pada list2",list2;
print "jumlah kata ini dalam list 3 ada sebanyak :", list4.count('ini');
print "Count for 123 : ", aList.count(123);
print "Count for zara : ", aList.count('zara');

