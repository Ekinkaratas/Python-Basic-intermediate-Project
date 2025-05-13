def create_tuple(x: int, y: int, z: int):
    new_list = [x,z,y]
    new_tuple = (min(new_list),max(new_list),sum(new_list))
    return new_tuple



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))