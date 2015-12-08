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

#ifndef INCLUDED_COWN_MISC_ADC_TAGS_GEN_IMPL_H
#define INCLUDED_COWN_MISC_ADC_TAGS_GEN_IMPL_H

#include <COWN_misc/adc_tags_gen.h>

namespace gr {
  namespace COWN_misc {

    class adc_tags_gen_impl : public adc_tags_gen
    {
     private:
      int counterp;
      int counter_shif;
      enum {SEARCH, COPY} d_state;

      unsigned long int timestamp;
      unsigned long int timestamp2;
      unsigned long int timestamp_meas;
      unsigned long int timestamp_meas2;

     public:
      adc_tags_gen_impl();
      ~adc_tags_gen_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

	  void insert_tag(uint64_t item);
	  
      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace COWN_misc
} // namespace gr

#endif /* INCLUDED_COWN_MISC_ADC_TAGS_GEN_IMPL_H */

