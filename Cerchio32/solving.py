"""
Attorno a un tavolo rotondo sono sedute, a distanza costante l’una dalla successiva, 32 persone.
In quanti modi e’ possibile scegliere 3 di loro in modo che a coppie non siano ne’ adiacenti ne’
diametralmente opposte?
"""

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Each group of people is represented by [i, j, k], where the number represents their position in the table


def tableSolve(x):
    # check if the number is valid
    if (x % 2) == 0 and x >= 6:
        possible = 0
        valid = 0
        # find all possible combinations which are not repeated

        # we use x - 2 instead of x because we want to leave space for the 2 people sitting after person 1
        for i in range(x - 2):
            for j in range(i + 1, x - 1):
                for k in range(j + 1, x):
                    # everytime we pass all 3 check we add 1 to the number of possible solutions
                    possible = possible + 1

                    # check if there are 2 people sitting close by
                    if j - i == 1 or k - j == 1 or (i == 0 and k == x - 1):
                        continue
                    # check if there are 2 people diametrically opposed
                    if i + x/2 == j or j + x/2 == k or i + x/2 == k:
                        continue
                    # if they aren't close AND they aren't diametrically opposed add 1 to the number of valid solutions
                    valid = valid + 1

        print("Number of possible combinations: " + str(possible))
        print("Number of valid combinations: " + str(valid))
    else:
        print("The number must be even AND the number must be at least 6.")


tableSolve(32)

