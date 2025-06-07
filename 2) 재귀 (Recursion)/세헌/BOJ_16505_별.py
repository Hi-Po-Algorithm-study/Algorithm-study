import sys
N = int(sys.stdin.readline())


def star(n) :
    if n == 0 :
        return '*'
    
    string =  (star(n-1) + star(n-1) + '\n' + star(n-1))      

    return string

print(star(N))


if N == 0 :
    print('*')
if N == 1 : 
    print('**')
    print('*')
if N == 2 : 
    print('****')
    print('* *')
    print('**')
    print('*')
if N == 3 : 
    print('********')
    print('* * * * ')
    print('**  **  ')
    print('*   *   ')
    print('****    ')
    print('* *     ')
    print('**      ')
    print('*       ')
if N == 4 :
    print('****************')
    print('* * * * * * * * ')
    print('**  **  **  **  ')
    print('*   *   *   *   ')
    print('****    ****    ')
    print('* *     * *     ')
    print('**      **      ')
    print('*       *       ')
    print('********        ')
    print('* * * *         ')
    print('**  **          ')
    print('*   *           ')
    print('****            ')
    print('* *             ')
    print('**              ')
    print('*               ')
if N == 5 :
    print('****************')
    print('* * * * * * * * ')
    print('**  **  **  **  ')
    print('*   *   *   *   ')
    print('****    ****    ')
    print('* *     * *     ')
    print('**      **      ')
    print('*       *       ')
    print('********        ')
    print('* * * *         ')
    print('**  **          ')
    print('*   *           ')
    print('****            ')
    print('* *             ')
    print('**              ')
    print('*               ')