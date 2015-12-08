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

#ifndef INCLUDED_AVIO505_ADC_THREE_CH_DEMUX_RTDEX_IMPL_H
#define INCLUDED_AVIO505_ADC_THREE_CH_DEMUX_RTDEX_IMPL_H

#include <avio505/adc_three_ch_demux_rtdex.h>

 #include <iostream>
#include <gnuradio/io_signature.h>

namespace gr {
  namespace avio505 {

    class adc_three_ch_demux_rtdex_impl : public adc_three_ch_demux_rtdex
    {
     private:
      unsigned short check_flag_bit;
      unsigned short flag_start;
      short *in_wo_header;
      float *in_to_floats;
      gr_complex *in_to_complex;
      int counter;
      int nit;


      unsigned long int timestamp;
      unsigned long int timestamp2;
      
      unsigned long int timestamp_meas;
      unsigned long int timestamp_meas2;
      

      
      
     public:
      adc_three_ch_demux_rtdex_impl();
      ~adc_three_ch_demux_rtdex_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace avio505
} // namespace gr

#endif /* INCLUDED_AVIO505_ADC_THREE_CH_DEMUX_RTDEX_IMPL_H */

