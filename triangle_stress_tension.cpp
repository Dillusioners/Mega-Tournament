/*
Author: LeeTuah
Date: 04 / 01 / 2023
For MegaEvent Event 2 Program 3
*/

# include <iostream>

int main(int argc, char const *argv[]){
    int triangle_count, vertices;

    std::cout << "How many triangles? ";
    std::cin >> triangle_count;
    triangle_count = abs(triangle_count);

    if(triangle_count % 2 == 0){
        vertices = 2*triangle_count;
    } else{
        vertices = 2*triangle_count+1;
    }

    for(int i = 1; i <= vertices; i++){
        if(i % 2 == 0) std::cout << '\\';
        else std::cout << ((i == vertices && triangle_count % 2 != 0)?' ' : '/');
    }
    std::cout << '\n' << "Number of Vertices: " << vertices;
    return 0;
}
