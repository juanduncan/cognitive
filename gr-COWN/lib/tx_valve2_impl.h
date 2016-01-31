/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_COWN_TX_VALVE2_IMPL_H
#define INCLUDED_COWN_TX_VALVE2_IMPL_H

#include <COWN/tx_valve2.h>

namespace gr {
  namespace COWN {

    class tx_valve2_impl : public tx_valve2
    {
     private:
          std::vector<gr::tag_t> d_tags;
      long packet_length; 

     public:
      tx_valve2_impl();
      ~tx_valve2_impl();

      // Where all the action really happens
      int work(int noutput_items,  
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace COWN
} // namespace gr

#endif /* INCLUDED_COWN_TX_VALVE2_IMPL_H */

