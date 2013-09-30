import sys
import maths
import puns
import text_gen

"""
dispatch user queries to appropriate functions
"""

# read from std in
# output to stdout?
#
# or is there a better way to communicate with the frontend process?

# assume the input is already split by the frontend code 
# TODO refactor to be more like a server, just read from std in
# then we can do something like
# cat cmds.txt | python dispatch.py
def main():
    if len(sys.argv) == 1:
        sanity_checks()
        exit(0)
    
    # dispatch based on user input.
    # TODO maybe think about put all the functions in in a
    # cmd -> function dictionary
    try:
        cmd = sys.argv[1]
        print cmd
        if cmd == "prime":
            print maths.is_prime(int(sys.argv[2]))
            
        elif cmd == "gcd":
            a = int(sys.argv[2])
            b = int(sys.argv[3])
            print maths.gcd(a, b)
        
        # make a pun
        elif cmd == "pun":
            print puns.make_pun()
            
        elif cmd == "text":
            assert sys.argc[2] == "like"
            # TODO join the text in the rest of the sys args
            print text_gen.generate_text(sys.argv[3])
            
    except:
        print "oh shit"



def sanity_checks():
    print len(sys.argv)
    print "sanity checks..."
    for i in xrange(1, 10):
        print "factorial(%d) = %d" % (i, maths.factorial(i))

main()
