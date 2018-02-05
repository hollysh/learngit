if __name__ == '__main__':
    filename=input('please input filename\m')
    with open(filename,'rt') as raw_data:
        with open(filename+'_fixed','wt' ) as fix_data:
            for line in raw_data:
                if line[-1].encode(ascii) == 3:
                    fix_data.write(line)
                else:
                    fixdata.write(line[0:-1])