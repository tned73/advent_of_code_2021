from typing import List, Dict


def read_file(filename="input_8.txt") -> List[str]:
    with open(filename, "r") as fh:
        total = []
        for line in fh.readlines():
            result = []
            print(line)
            for i in line.split('|'):
                result.append([''.join(sorted(j)) for j in i.split()])
            total.append(result)
    return total


def deduce_relation(param: List[str]) -> Dict[str,str]:
    def segments_on(number: str, segment: str) -> int:
        segments = 0
        for x in number:
            if x in segment:
                segments += 1
        return segments

    sor = sorted(param, key=lambda x: len(x))
    # print(sor)
    een = sor[0]
    zeven = sor[1]
    vier = sor[2]
    acht = sor[9]
    twee = ""
    vijf = ""
    twee_drie_vijf = sor[3:6]
    # print(twee_drie_vijf)
    for seg in twee_drie_vijf:
        if segments_on(een, seg) == 2:
            drie = seg
    twee_en_vijf = sor[3:6]
    twee_en_vijf.remove(drie)
    zes_negen_nul = sor[6:9]
    # print(zes_negen_nul)
    for seg in zes_negen_nul:
        # print(segments_on(vier, seg), seg)
        if segments_on(vier, seg) == 4:
            negen = seg
    zes_negen_nul.remove(negen)
    for seg in zes_negen_nul:
        # print(segments_on(een, seg), seg)
        if segments_on(een, seg) == 2:
            nul = seg
    zes_negen_nul.remove(nul)
    zes = zes_negen_nul[0]
    # print(twee_en_vijf)
    for seg in twee_en_vijf:
        # print(segments_on(seg, zes), seg, zes)
        if segments_on(seg, zes) == 5:
            vijf = seg
        if segments_on(seg, zes) == 4:
            twee = seg
    return {
        een: "1",
        twee: "2",
        drie: "3",
        vier: "4",
        vijf: "5",
        zes: "6",
        zeven: "7",
        acht: "8",
        negen: "9",
        nul: "0",
    }


def main():
    data = read_file()
    print(data)
    array = [0]*8
    total = 0
    for item in data:

        relation = deduce_relation(item[0])

        result = int(''.join([ relation[i] for i in item[1]]))
        print(result)
        total += result
        array[len(item)] += 1
    print(total)

if __name__ == "__main__":
    main()
