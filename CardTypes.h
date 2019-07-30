/**
 * \file CardTypes.h
 * \author Ridhwan Chowdhury, chowdr11, March 25th, 2019
 * \brief enumerates or defines certain types for implementation
 */
#ifndef A3_CARD_TYPES_H_
#define A3_CARD_TYPES_H_
/**
 * \brief Describes and enumerates the possible suits of a card
 */
enum SuitT {Heart, Diamond, Club, Spade};
/**
 * \brief Describes and enumerates each aspect of the gameboard 
 */
enum CategoryT {Tableau, Foundation, Deck, Waste};


#define TOTAL_CARDS 104



/**
 * \brief Describes the rank of a card.
 */
typedef unsigned short int RankT;

/**
 * \brief RankT for an Ace.
 */
#define ACE    1

/**
 * \brief RankT for an Jack.
 */
#define JACK   11


/**
 * \brief RankT for a Queen.
 */
#define QUEEN  12

/**
 * \brief RankT for a King.
 */
#define KING   13

/**
 * \brief Creates a structure in which SuitT and RankT can be used as instances s, and r
 */
struct CardT {
    SuitT s;
    RankT r;
};

/**
 * \brief Defines CardT as a type which is used in implementation 
 */
typedef struct CardT CardT;


#endif
