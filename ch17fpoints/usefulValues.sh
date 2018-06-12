#!/usr/bin/env bash

setUp() {
    set -e
}

buildSingleFormatSUT() {
    echo "
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
    if (argc < 2) {
        return 1;
    }
    unsigned int a = atoi(argv[1]); 
    float *b = 0x0;
    b = (float *)(&a);
    printf(\"0x%X -> %f\n\", a, *b);
    return 0;
}" > /tmp/_.c
    gcc -Wall -Werror /tmp/_.c -o /tmp/_
}

runSingleFormatSUT() {
    /tmp/_ $(( 16#FF800000 ))
    /tmp/_ $(( 16#C0000000 ))
    /tmp/_ $(( 16#BF800000 ))
    /tmp/_ $(( 16#BF000000 ))
    /tmp/_ $(( 16#80000000 )) 
    /tmp/_ $(( 16#3c8efa35 ))  # pi/180
    /tmp/_ $(( 16#3dcccccd )) 
    /tmp/_ $(( 16#3e9a209b ))  # log10(2) 
    /tmp/_ $(( 16#3ebc5ab2 ))  # 1/e
}

setUp
buildSingleFormatSUT
runSingleFormatSUT

