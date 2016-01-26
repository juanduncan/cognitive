/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
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

#ifndef INCLUDED_AVIO505_RESTA_IMPL_H
#define INCLUDED_AVIO505_RESTA_IMPL_H

#include <avio505/resta.h>

namespace gr {
  namespace avio505 {

    class resta_impl : public resta
    {
     private:
     int count_errors;
     int counter;
     long int mark_w;
     int diferencia;
     int last_input;
     //const int buf = 600;
      // Nothing to declare in this block.

     public:
      resta_impl();
      ~resta_impl();

      // Where all the action really happens
      
      //void set_history(int buf);
      
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace avio505
} // namespace gr

#endif /* INCLUDED_AVIO505_RESTA_IMPL_H */

