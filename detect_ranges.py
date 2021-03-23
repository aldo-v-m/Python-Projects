#!/usr/bin/env python3


def detect_ranges(L):

    sortList = sorted(L)
    newList = []
    i = 0

    while i < (len(sortList)-1):

        if sortList[i]+1 < sortList[i+1]:
            newList.append(sortList[i])
            i += 1
            inRange = False
            continue
        else:
            minLim = sortList[i]
            maxLim = minLim+2
            j = i+1
            inRange = True
            while inRange:
                if j == (len(sortList)-1):
                    insertRange = (minLim, maxLim)
                    newList.append(insertRange)
                    i = len(sortList)
                    break

                if sortList[j]+1 == sortList[j+1]:
                    maxLim += 1
                    j += 1

                else:
                    insertRange = (minLim, maxLim)
                    newList.append(insertRange)
                    i = j+1
                    inRange = False
    if inRange == False:
        newList.append(sortList[-1])
    return newList


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13, 15]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
