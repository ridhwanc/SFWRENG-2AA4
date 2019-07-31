/**
 * \file Gameboard.h
 * \brief This module is an abstract data type which allows multiple games to be created
 * \author Ridhwan Chowdhury, MacID: chowdr11
 * \date March 25, 2019
*/
#ifndef A3_GAME_BOARD_H_
#define A3_GAME_BOARD_H_

#include <vector>
#include "GameBoard.h"
#include "Stack.h"
#include "CardTypes.h"
#include "CardStack.h"

typedef std::vector<CardStackT> SeqCrdStckT;

class BoardT{
        /**
		 *  \brief local functions within the private so that are hidden from clints
		 */
    private:
        SeqCrdStckT T;
        SeqCrdStckT F;
        CardStackT D;
        CardStackT W;
        CardStackT tab_deck(std::vector<CardT> deck);
        bool valid_tab_tab(unsigned int n0, unsigned int n1);
        bool tab_placeable(CardT c, CardT d);
        bool valid_tab_foundation(unsigned int n0, unsigned int n1);
        bool foundation_placeable(CardT c, CardT n1);
        bool is_valid_pos(CategoryT c, unsigned int n);
        bool valid_waste_tab(unsigned int n);
        bool valid_waste_foundation(unsigned int n);


    public:
        BoardT();
        BoardT(std::vector<CardT>);
        bool is_valid_tab_mv(CategoryT, int, int);
        bool is_valid_waste_mv(CategoryT c, unsigned int n);
        bool is_valid_deck_mv();
        void tab_mv(CategoryT c, int n0, int n1);
        void waste_mv(CategoryT c, int n);
        void deck_mv();
        /**
		 *  \brief retrieves the card from the tableau
		 *  \param i is the index which represents a specific card in the tableau stack
         *  \return returns the indexed card of the tableau
		 */
        CardStackT get_tab(unsigned short int i);
        /**
		 *  \brief retrieves the card from the foundation
		 *  \param i is the index which represents a specific card in the foundation stack 
         *  \return returns the indexed card of the foundation
		 */
        CardStackT get_foundation(int i);
        /**
		 *  \brief retrieves the deck 
         *  \return returns the cards from deck
		 */
        CardStackT get_deck();
        /**
		 *  \brief retrieves the deck 
         *  \return returns the cards from deck
		 */
        CardStackT get_waste();
         /**
		 *  \brief retrieves the deck 
         *  \return returns the cards from deck
		 */
        bool valid_mv_exists();
        bool is_win_state();



}

#endif
