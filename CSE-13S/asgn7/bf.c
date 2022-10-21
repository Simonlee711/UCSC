#include "bf.h"

#include "bv.h"
#include "speck.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct BloomFilter {
    uint64_t primary[2]; //  Primary  hash  function  salt.
    uint64_t secondary[2]; //  Secondary  hash  function  salt.
    uint64_t tertiary[2]; //  Tertiary  hash  function  salt.
    BitVector *filter;
};

// straight from assignment document
BloomFilter *bf_create(uint32_t size) {
    BloomFilter *bf = (BloomFilter *) malloc(sizeof(BloomFilter));
    if (bf) {
        //  Grimm's Fairy  Tales
        bf->primary[0] = 0x5adf08ae86d36f21;
        bf->primary[1] = 0xa267bbd3116f3957;
        // The  Adventures  of  Sherlock  Holmes
        bf->secondary[0] = 0x419d292ea2ffd49e;
        bf->secondary[1] = 0x09601433057d5786;
        // The  Strange  Case of Dr. Jekyll  and Mr. Hyde
        bf->tertiary[0] = 0x50d8bb08de3818df;
        bf->tertiary[1] = 0x4deaae187c16ae1d;
        bf->filter = bv_create(size);
        if (!bf->filter) {
            free(bf);
            bf = NULL;
        }
    }
    return bf;
}

void bf_delete(BloomFilter **bf) {
    if (bf) {
        free(*bf);
        bf = NULL;
    }
}

uint32_t bf_size(BloomFilter *bf) {
    uint32_t length = bv_length(bf->filter);
    return length;
}

//Sahiti's Section logic
void bf_insert(BloomFilter *bf, char *oldspeak) {
    //hash and set salts to specifed bits
    uint32_t index1 = hash(bf->primary, oldspeak) % bf_size(bf);
    bv_set_bit(bf->filter, index1);
    uint32_t index2 = hash(bf->secondary, oldspeak) % bf_size(bf);
    bv_set_bit(bf->filter, index2);
    uint32_t index3 = hash(bf->tertiary, oldspeak) % bf_size(bf);
    bv_set_bit(bf->filter, index3);
}

//Sahiti's section logic
bool bf_probe(BloomFilter *bf, char *oldspeak) {
    //hash and see if salts are set
    uint32_t index1 = hash(bf->primary, oldspeak) % bf_size(bf);
    uint32_t first = bv_get_bit(bf->filter, index1);
    uint32_t index2 = hash(bf->secondary, oldspeak) % bf_size(bf);
    uint32_t sec = bv_get_bit(bf->filter, index2);
    uint32_t index3 = hash(bf->tertiary, oldspeak) % bf_size(bf);
    uint32_t third = bv_get_bit(bf->filter, index3);
    if ((first != 0) && (sec != 0) && (third != 0)) {
        return true;
    }
    return false;
}

//Sabrina's section logic
uint32_t bf_count(BloomFilter *bf) {
    uint32_t counter = 0;
    for (uint32_t i = 0; i < bv_length(bf->filter); i++) {
        if (bv_get_bit(bf->filter, i) != 0) {
            counter += 1;
        }
    }
    return counter;
}

void bf_print(BloomFilter *bf) {
    bv_print(bf->filter);
}
