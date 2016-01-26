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

#ifndef INCLUDED_AVIO505_THREE_CH_MULTIP_RTDEX_IMPL_H
#define INCLUDED_AVIO505_THREE_CH_MULTIP_RTDEX_IMPL_H

#include <avio505/three_ch_multip_rtdex.h>

namespace gr {
  namespace avio505 {

    class three_ch_multip_rtdex_impl : public three_ch_multip_rtdex
    {
     private:
      short *dme1_shorts;
      short *dme2_shorts;
      short *adsb_shorts;
      float *dme1_floats;
      float *dme2_floats;
      float *adsb_floats;

      unsigned short flag_start; 
      unsigned short clear_first4bits;
      // Nothing to declare in this block.

     public:
      three_ch_multip_rtdex_impl();
      ~three_ch_multip_rtdex_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);
 

      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace avio505
} // namespace gr

#endif /* INCLUDED_AVIO505_THREE_CH_MULTIP_RTDEX_IMPL_H */

